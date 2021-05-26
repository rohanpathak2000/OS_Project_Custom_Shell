echo "  ======= *********************** ========  "
echo "=========  Welcome to our Portal =========="
echo "  ======= *********************** ========  "
echo ""
echo " Are you a : "
echo " 1. Customer "
echo " 2. Transporter "
echo " 3. Shopkeeper "
printf "Enter choice : "
read ch

if [ $ch -eq 1 ] 
then
	start python customer.py
elif [ $ch -eq 2 ]
then
	start python transporter.py
elif [ $ch -eq 3 ]
then
	start python shopkeeper.py

fi 

