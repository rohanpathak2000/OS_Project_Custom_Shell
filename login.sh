echo ""
echo "Press 1 to login as Consumer"
echo "Press 2 to login as Shopkeeper"
echo "Enter choice : "
read consumer_or_shopkeeper

if [ $consumer_or_shopkeeper -eq 1 ]
then
	bash consumer_home_page.sh
else 
	printf "\nEnter Shopkeeper Id : "
	read shopkeeper_id
	if [ $shopkeeper_id -eq 50 ]
	then
		bash shopkeeper_home_page.sh
	else
		printf "\n Incorrect Shopkeeper id\n Enter correct id "
	fi
fi
		
	

