#include <iostream>
#include <stdlib.h>
#include <random>
using namespace std;

int main(){
	//DEFAULT VARIABLES
	//string	msg="gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"; //7
	//string	msg="vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"; //3
	//string msg="Klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojice\
mlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmrioc\
wpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn";
	string 	msg = "abcdefghijklmnopqrstuvwxyz";
	char 	letters[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
							'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	//CESAR CYPHER
	int 	shift = 7;

	//KEY CYPHER
	string	wordKey = "bbb";
	
	//RANDOM SEED CYPHER
	int		seed = 123;
	
	//FUNCOES
	void encriptCesar(string msg, int shift, char letters[]);
	void decriptCesar(string msg, int shift, char letters[]);
	void encriptKey(string msg, string key, char letters[]);
	void decriptKey(string msg, string key, char letters[]);	
	void encriptSeed(string msg, int shift, char letters[], int seed);
	void decriptSeed(string msg, int shift, char letters[], int seed);
	
	//CODIGO	
	cout << "/*--------------------------------*/" << endl;
	cout << "/*----------Encriptemos-----------*/" << endl;
	cout << "/*--------------------------------*/" << endl;
	cout << "/*-----Writed by: Mayk Caldas-----*/" << endl;
	cout << "/*-------in a friday morning------*/" << endl;
	cout << "/*--------------------------------*/" << endl;
	
	cout << endl << "Your message was:" << endl;
	cout << msg << endl << endl;
	
	cout << "USING CESAR CYPHER" << endl << endl;
	
	//encriptCesar(msg, shift, letters);
	/*for(int i=0;i<26;i++){
		shift=i;
		decriptCesar(msg, shift, letters);
	}*/
	encriptCesar(msg, shift, letters);
	decriptCesar(msg, shift, letters);
	
	cout << "USING KEY CYPHER" << endl << endl;
	
	encriptKey(msg, wordKey, letters);
	decriptKey(msg, wordKey, letters);
	
	cout << "USING RANDOM SEED CYPHER" << endl << endl;
	
	encriptSeed(msg, shift, letters, seed);
	decriptSeed(msg, shift, letters, seed);
	
	return 0;
}

void encriptCesar(string msg, int shift, char letters[]){
	string cypher="";
	
	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				//cypher+=letters[(((1+(abs(shift)/26))*26)+j+shift)%26];
				cypher+=letters[( (1+(abs(shift)/26))*26 + (j+shift) )%26];
				break;
			}
			if(j==25){
				cypher+=" ";
			}
		}
		
	}
	
	cout << endl << "Encriptando ela com o shift fixo igual a " << shift << ":"<< endl;
	cout << cypher << endl << endl;
}

void decriptCesar(string msg, int shift, char letters[]){
	string cypher="";
	
	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				//cypher+=letters[(((1+(abs(shift)/26))*26)+j-shift)%26];
				cypher+=letters[( (1+(abs(shift)/26))*26 + (j-shift) )%26];
				break;
			}
			if(j==25){
				cypher+=" ";
			}
		}
		
	}
	
	cout << endl << "Decriptando ela com o shift fixo igual a " << shift << ":"<< endl;
	cout << cypher << endl << endl;
}

void encriptKey(string msg, string wordKey, char letters[]){
	string	cypher="";
	string	key="";
	int 	shift=0;
	
	while(key.size()<msg.size()){
		for(int l=0; l<(wordKey.size()); l++){
			key+=wordKey[l];
		}
	}
	
	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(key[i]==letters[j]){
				shift=j;
			}
		}
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				cypher+=letters[(((1+(abs(shift)/26))*26)+j+shift)%26];
			}
		}
	}

	cout << "Encriptando ela com a chave " << wordKey << ":" << endl;
	cout << cypher << endl << endl;
}

void decriptKey(string msg, string wordKey, char letters[]){
	string	cypher="";
	string	key="";
	int 	shift=0;
	
	while(key.size()<msg.size()){
		for(int l=0; l<(wordKey.size()); l++){
			key+=wordKey[l];
		}
	}
	
	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(key[i]==letters[j]){
				shift=j;
			}
		}
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				cypher+=letters[(((1+(abs(shift)/26))*26)+j-shift)%26];
			}
		}
	}

	cout << "Decriptando ela com a chave " << wordKey << ":" << endl;
	cout << cypher << endl << endl;
}

void encriptSeed(string msg, int shift, char letters[], int seed){
	string cypher="";
	mt19937	rand1(seed);
	uniform_int_distribution<> dis1(0, 25);
	
	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				cypher+=letters[( (1+(abs(dis1(rand1)))/26)*26 + (j+dis1(rand1)) )%26];
				break;
			}
			if(j==25){
				cypher+=" ";
			}
		}
	}
	
	cout << endl << "Encriptando ela com a semente " << seed << ":"<< endl;
	cout << cypher << endl << endl;
}

void decriptSeed(string msg, int shift, char letters[], int seed){
	string cypher="";
	mt19937	rand2(seed);
	uniform_int_distribution<> dis2(0, 25);

	for(int i=0; i<msg.size(); i++){
		for(int j=0; j<26; j++){
			if(msg[i]==letters[j]){
				cypher+=letters[( (1+(abs(dis2(rand2))/26))*26 + (j-dis2(rand2)) )%26];
				break;
			}
			if(j==25){
				cypher+=" ";
			}
		}
	}
	
	cout << endl << "Decriptando ela com a semente " << seed << ":"<< endl;
	cout << cypher << endl << endl;
}
