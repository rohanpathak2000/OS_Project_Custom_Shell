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
	python customer.py
elif [ $ch -eq 2 ] 
then
	python transporter.py
elif [ $ch -eq 3 ] 
then
	python shopkeeper.py
fi 
