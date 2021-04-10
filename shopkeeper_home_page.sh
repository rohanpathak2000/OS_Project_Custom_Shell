echo " Shopkeeper Home Page " 
echo "                                             "
echo "Press Following Keys for Following Operations"
echo "                                             "
echo "1)	View pending Orders"
echo "2)    Mark for pickup"
echo "											   "

read operation_number

if [ $operation_number -eq 1 ]
then
    echo "                                         "
    echo "Enter Your shop Id"
    echo "                                         "
	read shop_id
    if [ $shop_id -eq 1 ]
	then
	   echo "                                             "
	   echo "Enter Order Id"
	   echo "                                             "

	   read search_order

	   echo "                                             "
	   echo " *****************  Pending Orders *******************"
	   grep  $search_order orders.txt
	   echo "                                             "
	elif [ $shop_id -eq 2 ]
	then
	   echo "                                             "
	   echo "Enter Order Id"
	   echo "                                             "

	   read search_order

	   echo "                                             "
	   echo " *****************  Pending Orders *******************"
	   grep  $search_order orders.txt
	   echo "                                             "
	fi
elif [ $operation_number -eq 2 ]
then
	echo "                                              "
	python item_dispatch.py
	echo "	                                            "
fi