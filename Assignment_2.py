import pygame
import time
#Sulaiman Nezami
#100869554
pygame.mixer.init()

def load_swap_sound():
    # Swoosh Sound effect that will play after every merge.
    swap_sound = pygame.mixer.Sound("SWOOSH.wav")
    return swap_sound

#Merging the function to combine the two subarrays within the arr[]
def merge(arr, l, m, r, swap_sound):
    L = arr[l:m+1]
    R = arr[m+1:r+1]

    # Now its time to merge the temp arrays back into arr[l..r]
    i = j = 0
    k = l

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            # Play sound effect for swap
            swap_sound.play()
            # Wait for the sound effect to finish because if not, 
            # then it will just make one big swoosh sound, 
            # and you wouldn't hear the swoosh for every step.
            time.sleep(0.2)
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1 # this one will move to the next element in L
        k += 1 # this one will Move to the next position in the original array 

    while j < len(R):
        arr[k] = R[j]
        # this one will also now move to the next element in R
        j += 1 
        # This one will move the next position inside the ORIGINAL array..
        k += 1

# Main function to implement Merge Sort
def mergeSort(arr, left, right, swap_sound):
    if left < right:

        # Finding the middle point and dividing by 2
        mid = (left + right) // 2

        # Sort first halve and then the second halves, 
        # whilst also putting in the swap sound effect we implemented into earlier
        mergeSort(arr, left, mid, swap_sound)
        mergeSort(arr, mid + 1, right, swap_sound)

        # showing the next steps before merge, and one it merges .....
        print("Next step: {} | {}".format(arr[left:mid + 1], arr[mid + 1:right + 1]))

        # .... it will Merge the sorted halves and then .....
        merge(arr, left, mid, right, swap_sound)

        # .... it will print current state of array to show what is so far merged.
        print("Merging:", arr[left:right + 1])
        time.sleep(0.2) #this is to make sure that it is in the same time when the swapping sound effect takes place, 
        #it doesn't go so quickly that we miss it. (we can adjust this) 

# We can put an ything inside this array just has to be a number.
arr = [3, 5, 6, 2, 7, 1, 4, 9]
n = len(arr)

# Print original array
print("Product ID:", arr)

# Loading the swap sound effect
swap_sound = load_swap_sound()

# Perform the Merge Sort and printing each step after..
print("Merge Sort Steps:")
mergeSort(arr, 0, n - 1, swap_sound)

# .. Final sorted array with it being in a increasing order :)
print("Final sorted array:", arr)