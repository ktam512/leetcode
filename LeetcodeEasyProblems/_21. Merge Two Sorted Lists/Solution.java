public class Solution {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //Create a head node so that latter we can return tempNode.next
        //to have the head of the final list right away
        ListNode tempNode = new ListNode(0);
        ListNode curNode = tempNode;




        //The loop keep running until one of the list is empty
        while(list1!= null && list2!= null){
            if(list1.val < list2.val){
                curNode.next = list1;
                list1 = list1.next;
            } else {
                curNode.next = list2;
                list2 = list2.next;
            }

            curNode = curNode.next;

        }

        //When one of the list is empty, we take the final part of the non-empty
        //list and insert it into our in-progress building merged list
        if(list1 == null){
            while(list2 != null){
                curNode.next = list2;
                list2 = list2.next;
                curNode = curNode.next;
            }
        } else{
            while(list1 != null){
                curNode.next = list1;
                list1 = list1.next;
                curNode = curNode.next;
            }
        }





        return tempNode.next;


        
        
    }

    //Example: 
    //Input: list1 = [1,2,4], list2 = [1,3,4]
    //Output: [1,1,2,3,4,4]

    public static void main(String[] args) {
        ListNode list1 = new ListNode(
            1,new ListNode(2,new ListNode(4))
        );
        // list1.insert(1);
        // list1.insert(2);
        // list1.insert(4);
        
        
        ListNode list2 = new ListNode(
            1,new ListNode(3,new ListNode(4))
        );
        // list1.insert(1);
        // list1.insert(3);
        // list1.insert(4);

        ListNode mergedList = mergeTwoLists(list1, list2);

        System.out.println(mergedList);

        
    }


}