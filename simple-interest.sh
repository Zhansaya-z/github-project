#!/bin/bash

echo "=== Simple Interest Calculator ==="

read -p "Enter principal amount: " principal
read -p "Enter rate of interest: " rate
read -p "Enter time period (in years): " time

interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
total=$(echo "scale=2; $principal + $interest" | bc)

echo ""
echo "--- Results ---"
echo "Principal Amount: $principal"
echo "Rate of Interest: $rate%"
echo "Time Period: $time years"
echo "Simple Interest: $interest"
echo "Total Amount: $total"
