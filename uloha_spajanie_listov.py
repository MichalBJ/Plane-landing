def join_list_with_sort(list_1, list_2):
    final_list = []
    for c in list_1:
        final_list.append(c)

    for c in list_2:
        final_list.append(c)

    final_list.sort()
    return final_list


def join_list(list1, list2):
    final_list = []
    for c in list1:
        final_list.append(c)

    for c in list2:
        final_list.append(c)

    for x, value in enumerate(final_list):
        a = value
        b = x
        pass




nums1 = [1, 2, 4]
nums2 = [2, 3, 6]


zoznam = join_list_with_sort(nums1, nums2)

for p in zoznam:
    print(p)