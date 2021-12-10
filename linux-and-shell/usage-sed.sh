echo "print the categories:"
cat data/category.txt

echo "\n\nsed guava appending at the position 2"
sed '2aguava' data/category.txt

echo "\n\nsed pear inserting a new line at the position 4"
sed '4ipear' data/category.txt

echo "\n\ndelete the 5th line"
sed '5d' data/category.txt

echo "\n\ndelete the 2nd-4th line"
sed '2,4d' data/category.txt

echo "\n\nreplace an a by x for each line"
sed 's#a#x#' data/category.txt

echo "\n\nreplace all a by A for each line"
sed 's#a#A#g' data/category.txt
