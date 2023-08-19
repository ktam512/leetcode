public class Main {
    public static void main(String[] args) {
        int [][]image = new int [][]{{1,1,1},{1,1,0},{1,0,1}};
        int sr = 1;
        int sc = 1;
        int newColor = 2;
        floodFill(image,sr,sc,newColor);
        int hehe = 0;
    }

    public static int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if(image[sr][sc] == newColor) return image;
        fill(image, sr , sc, image[sr][sc], newColor);
        return image;


    }

    public static void fill(int[][] image, int sr, int sc, int color, int newColor) {
        if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length
        || image[sr][sc] != color){
            return;
        }
        image[sr][sc] = newColor;
        fill(image, sr - 1, sc, color, newColor);
        fill(image, sr + 1, sc, color, newColor);
        fill(image, sr , sc - 1, color, newColor);
        fill(image, sr , sc + 1, color, newColor);


    }
}