using System;
using System.Collections.Generic;

class Program
{
    // Insertion sort function to sort individual buckets
    static void InsertionSort(List<float> bucket)
    {
        for (int i = 1; i < bucket.Count; ++i)
        {
            float key = bucket[i];
            int j = i - 1;
            while (j >= 0 && bucket[j] > key)
            {
                bucket[j + 1] = bucket[j];
                j--;
            }
            bucket[j + 1] = key;
        }
    }

    // Function to sort arr[] of size n using bucket sort
    static void BucketSort(float[] arr)
    {
        int n = arr.Length;

        // 1) Create n empty buckets
        List<float>[] buckets = new List<float>[n];
        for (int i = 0; i < n; i++)
        {
            buckets[i] = new List<float>();
        }

        // 2) Put array elements in different buckets
        for (int i = 0; i < n; i++)
        {
            int bi = (int)(n * arr[i]);
            buckets[bi].Add(arr[i]);
        }

        // 3) Sort individual buckets using insertion sort
        for (int i = 0; i < n; i++)
        {
            InsertionSort(buckets[i]);
        }

        // 4) Concatenate all buckets into arr[]
        int index = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < buckets[i].Count; j++)
            {
                arr[index++] = buckets[i][j];
            }
        }
    }

    // Driver program to test above function
    static void Main(string[] args)
    {
        float[] arr = { 0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f };
        BucketSort(arr);

        Console.WriteLine("Sorted array is:");
        foreach (float num in arr)
        {
            Console.Write(num + " ");
        }
    }
}
