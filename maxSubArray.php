<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumSubarraySum($nums, $k)
    {
        $sub_array = [];
        for ($i = 0; $i < $k; $i++) {
            $sub_array[$i] = 0;
        }

        $size = count($sub_array);
        foreach ($nums as $num) {
            echo $num . " ";
        }
        echo "<br>The size = " . $size;
    }
}

$sol = new Solution();

$nums = [1, 5, 4, 2, 9, 9, 9];
$k = 3;

$sol->maximumSubarraySum($nums, $k);
