for i in {1..120};do wget -nc https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds/$i; done
clear
chmod +x pylarCore.py
clear
python3 pylarCore.py > results.pylar
clear
echo "Done ✅ Go to podium.pylar and results.pylar to see the results."