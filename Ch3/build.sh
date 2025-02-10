#!/bin/bash
echo "Compiling:"
g++ -std=c++11 Ch3P4.cpp; 
echo "compiled. Running:";
./a.out; 
echo "Runned. Removing:";
rm ./a.out;
echo "Removed";