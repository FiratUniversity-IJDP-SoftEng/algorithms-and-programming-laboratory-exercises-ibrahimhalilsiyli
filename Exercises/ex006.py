# Your Student ID:  240543022
# Your Name and Surname:  IBRAHIM HALIL SIYLI
original_list = list(range(1, 11))

print(original_list)                                #1.Print the original list

reverse_list = original_list[::-1]
print(reverse_list)                                 #2.Reverse the list and print it

added_reverse_list = reverse_list + [11,12,13]

print(added_reverse_list )                          #3.Add the numbers 11, 12, and 13 to the list and print it(reversed)
print(len(added_reverse_list ))                     #4.Print the list's length

removed_list = added_reverse_list[1:-1]
print(removed_list)                                 #5.Remove the first and last elements, then print the list

even_list= original_list[1::2]
print(even_list)                                    #6.Create and print a new sorted list containing only even numbers from the original list


