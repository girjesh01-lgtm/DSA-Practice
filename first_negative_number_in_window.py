from collections import deque


def first_negative_number_in_window(arr, k):
    left = 0
    right = k-1
    queue = deque()


    for right in range(len(arr)):
        if arr[right] < 0:
            queue.append(arr[right])

        if right >= k - 1:
            if len(queue) == 0:
                print(0)
            elif queue[0] == arr[left]:
                print(queue[0])
                queue.popleft()
            else:
                print(queue[0])

            left += 1






#first_negative_number_in_window([12,-1,-7,8,-15,30,16,28,-5], 3)

#first_negative_number_in_window([1,-2,-2,3],2)

#arr = [-2, 5, -2, 3]
#k = 2

#arr = [-2, -3, 4, -3]
#k = 2

arr = [-2, 5, -2, -2]
k = 2


first_negative_number_in_window(arr, k)