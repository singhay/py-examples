import java.util.List;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

    }

    private int[] threeSumH(int[] nums, int[] rest) {
        int sum = 0;
        int[] triplets = new int[];
        int[] temp = new int[];
        for (int i = 0; i < rest.length; i++)
            sum += rest[i];

        if (sum==0 && rest.length==3) return rest;
        for(int a : nums) {
            triplets[0] = a;
            for (int i = 0; i < rest.length; i++)
                triplets[i] = rest[i];
            if (a+sum==0 && triplets.length==3)
                return triplets;
            temp = nums;
            temp
        }
        return triplets;
    }
}
