{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Script to implement an alogirthm to determine if a string has unique characters or not\n",
    "# This assumes that the input to the function is sorted. It uses Binary Search to find the element while we traverse through\n",
    "# the array\n",
    "\n",
    "import pdb\n",
    "\n",
    "def BinarySearch(ip,target):\n",
    "    first=0\n",
    "    last=len(ip)-1\n",
    "    # Check for input length\n",
    "    if len(ip) == 0:\n",
    "        return False\n",
    "    elif len(ip) == 1:\n",
    "        if ip[0] == target:\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "    \n",
    "    while (first<=last):\n",
    "        middle = (first+last)//2\n",
    "        if ip[middle] == target:\n",
    "            return True\n",
    "        elif ip[middle] < target:\n",
    "            first=middle+1\n",
    "        elif ip[middle] > target:\n",
    "            last=middle-1\n",
    "    \n",
    "    return False\n",
    "\n",
    "# Function to check if the string is unique or not\n",
    "def isUnique(ip):\n",
    "    \n",
    "    found = False # Flag to check if a 2nd element is found\n",
    "    # Iterate through the array\n",
    "    for i,x in enumerate(ip):\n",
    "        if BinarySearch(ip[i+1:],x):\n",
    "            found= True\n",
    "        else:\n",
    "            continue\n",
    "        \n",
    "    if found:\n",
    "        return False\n",
    "    else:\n",
    "        return True\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(isUnique([\"a\",\"b\",\"c\",\"c\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
