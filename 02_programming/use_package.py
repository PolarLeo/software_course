from example_package_leonard import example
print(example.add_one(1))

from example_package_leonard import reverse_list
a = 'VOG!lo olH'
b = 'el,Wrd ROY'
print(reverse_list.reverse_function(a))

from example_package_leonard import merge_lists
print(merge_lists.merge_function(a,b))

from example_package_leonard import str2bin
print('encoded string:')
print(str2bin.str2bin_function(a))

print('decoded file:')
print(str2bin.bin2str_function("string.bin"))

from example_package_leonard import plotting_example
plotting_example.example_plot()
