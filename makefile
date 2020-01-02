.PHONY: small_pic
.PHONY: big_pic


small_pic:
	./main.py -i gimp_out/small1.png -e gimp_out/big1.png -f ./fig/oko.png

big_pic:
	./main.py -i gimp_out/small2.png -e gimp_out/big2.png -f ./fig/01.png