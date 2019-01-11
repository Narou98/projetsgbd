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
	if(i_flag==1){
		if(strcmp(format_fichier, "xml")==0 || strcmp(format_fichier,"json")==0){
			if(h_flag==1 ^ f_flag==1){
				if(o_flag==1){
					if(t_flag){
					printf("vous avez des traces\n");
				printf("Analyse du fichier de sortie\n");
				}
				else{
					printf("Renseigner un argument pour la sortie SVP!\n");
					exit(1);
				}
			}
			else{
				printf("Renseigner une entree <-h flux http | -f fichier>\n");
				exit(2);
			}
		}
		else{
			printf("Renseigner le format du fichier en entree <-i xml|json >\n");
			exit(3);
		}
	}
	else{
		printf("Renseigner le format en entree\n");
		exit(4);
	}
	return 0;
}
}
    

