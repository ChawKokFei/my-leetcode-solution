/*
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
*/
using System.Numerics;
using System.Runtime.InteropServices;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        Console.WriteLine(solution.binaryCalculation("1111", "1111"));
    }

    public string binaryCalculation(string a, string b)
    {
        StringBuilder result = new StringBuilder();

        int pointerA = a.Length - 1;
        int pointerB = b.Length - 1;
        int carryOver = 0;

        while (pointerA >= 0 || pointerB >= 0 || carryOver == 1)
        {
            int sum = carryOver;

            if (pointerA >= 0)
            {
                sum += a[pointerA] - '0';
                --pointerA;
            }

            if (pointerB >= 0)
            {
                sum += b[pointerB] - '0';
                --pointerB;
            }

            carryOver = sum / 2;

            result.Insert(0, sum % 2);
        }

        return result.ToString();
    }
}