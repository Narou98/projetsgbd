#include<stdio.h>
#include<stdlib.h>
#include<getopt.h>

int main(int argc , char *argv) 
{
	//les options en ligne de commande
	int option; 
	//declaration des variables
	int i_flag=0;
	int t_flag=0;  
	int h_flag=0;
	int f_flag=0;  
	int o_flag=0;
	char *format_fichier;
	while ((option = getopt(argc , argv, "i:t:h:f:o")) != -1) //"ithfo" les options permises
	{
		switch (option)
		{
			case 'i':
				i_flag++;
				format_fichier=optarg; // optarg variable qui stocke l'argument d'une option
				break;
			case 't':
				t_flag++;
				break;
			case 'h':
				h_flag++;
				break;
			case 'f':
				f_flag++;
				break;
			case 'o':
				o_flag++;
				break;
			default:
				printf();
		} 	
	}
}
