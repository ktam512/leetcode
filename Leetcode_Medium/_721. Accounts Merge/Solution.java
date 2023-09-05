import java.util.*;

class UnionFind {
    private int[] par;
    private int[] rank;

    public UnionFind(int n) {
        par = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            par[i] = i;
            rank[i] = 1;
        }
    }

    public int find(int x) {
        while (x != par[x]) {
            par[x] = par[par[x]];
            x = par[x];
        }
        return x;
    }

    public boolean union(int x1, int x2) {
        int p1 = find(x1);
        int p2 = find(x2);
        if (p1 == p2) {
            return false;
        }
        if (rank[p1] > rank[p2]) {
            par[p2] = p1;
            rank[p1] += rank[p2];
        } else {
            par[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
    }
}

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        UnionFind uf = new UnionFind(accounts.size());
        Map<String, Integer> emailToAccountIndex = new HashMap<>();
        Map<Integer, List<String>> emailGroup = new HashMap<>();

        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                if (emailToAccountIndex.containsKey(email)) {
                    uf.union(i, emailToAccountIndex.get(email));
                } else {
                    emailToAccountIndex.put(email, i);
                }
            }
        }

        for (String email : emailToAccountIndex.keySet()) {
            int accountIndex = emailToAccountIndex.get(email);
            int leader = uf.find(accountIndex);
            emailGroup.putIfAbsent(leader, new ArrayList<>());
            emailGroup.get(leader).add(email);
        }

        List<List<String>> result = new ArrayList<>();
        for (int leader : emailGroup.keySet()) {
            List<String> mergedAccount = new ArrayList<>();
            List<String> emails = emailGroup.get(leader);
            Collections.sort(emails);
            String name = accounts.get(leader).get(0);
            mergedAccount.add(name);
            mergedAccount.addAll(emails);
            result.add(mergedAccount);
        }

        return result;
    }
}
