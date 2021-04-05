echo " "
echo " 1. View all the available items  "
echo " 2. Search an item "
echo " 3. Place an Order "
printf "Enter Choice : "
read ch
if [ $ch -eq 1 ]
then
	cat items.txt	
elif [ $ch -eq 2 ]
then
	echo ""
	echo "1. Lookup Category "
	echo "2. Lookup Product Name "
	printf "Enter Choice : " 
	read search_method
	if [ $search_method -eq 1 ]
	then
		echo "Select from the given categories"
		echo "1. Fruits"
		echo "2. Dairy"
		printf "\nEnter Choice : "
		read category_choice
		if [ $category_choice -eq 1 ]
		then
			grep "fruits" items.txt
		elif [ $category_choice -eq 2 ]
		then
			grep "dairy" items.txt
		fi		
		
	elif [ $search_method -eq 2 ]
	then	
		printf "\nEnter Name : "
		read query_name
		grep -i $query_name items.txt
	fi
elif [ $ch -eq 3 ]
then
	python give_order.py
fi

	