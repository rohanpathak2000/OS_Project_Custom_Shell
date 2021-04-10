echo "                                             "
echo "Press Following Keys for Following Operations"
echo "                                             "
echo "1)	View Undelivered Orders                "
echo "2)    Confirm Delivery                       "
echo "											   "

read operation_number

if [ $operation_number -eq 1 ]
then
    echo "                                             "
    echo "Enter Your transporter Id"
    echo "                                             "
    read trp_id
	
    if [ $trp_id -eq 7 ]
	then
	   echo "                                             "
	   echo "Enter Order Id"
	   echo "                                             "

	   read search_order

	   echo "                                             "
	   echo " *****************  Pending Orders *******************"
	   grep  $search_order transp.txt
	   echo "                                             "
	elif [ $trp_id -eq 8 ]
	then
	   echo "                                             "
	   echo "Enter Order Id"
	   echo "                                             "

	   read search_order

	   echo "                                             "
	   echo " *****************  Pending Orders *******************"
	   grep  $search_order transp2.txt
	   echo "                                             "
	fi
elif [ $operation_number -eq 2 ]
then
	echo "                                              "
	python delivery_confirmed.py
	echo "	                                            "
fi