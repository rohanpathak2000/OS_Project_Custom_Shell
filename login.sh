echo ""
echo "Press 1 to login as Consumer"
echo "Press 2 to login as Shopkeeper"
echo "Press 3 to login as Transporter"
echo "Enter choice : "
read consumer_or_shopkeeper

if [ $consumer_or_shopkeeper -eq 1 ]
then
	bash consumer_home_page.sh
elif [ $consumer_or_shopkeeper -eq 2 ]  
then
	printf "\nEnter Shopkeeper Id : "
	read shopkeeper_id
	if [ $shopkeeper_id -eq 50 ]
	then
		bash shopkeeper_home_page.sh
	else
	    printf "\n Incorrect Shopkeeper id\n Enter correct id "
	fi
elif [ $consumer_or_shopkeeper -eq 3 ]
then
    printf "\nEnter Transporter Id :"
	read transporter_id
	if [ $transporter_id -eq 20 ]
	then
		bash transporter_home_page.sh
	else
	    printf "\n Incorrect Transporter id\n Enter correct id "
	fi
fi
		
	

