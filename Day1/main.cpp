#include <fstream>
#include <iostream>
#include <string>
int main()
{
	int count = 0, Max1 = 0, Max2 = 0, Max3 = 0; bool breakCount = false; std::ifstream file; std::string line;
	file.open("key.txt");
	while (std::getline(file, line))
	{
		if (line == "") { breakCount = true; }
		else { count += std::stoi(line); }
		if (file.eof()) { breakCount = true; }
		if (breakCount) {
			if (Max1 < count) { Max3 = Max2; Max2 = Max1; Max1 = count; }
			else if (Max2 < count) { Max3 = Max2; Max2 = count; }
			else if (Max3 < count) { Max3 = count; }
			count = 0; breakCount = false;
		}
	}
	printf("Max1: %d Max2: %d Max3: %d and their sum: %d\n", Max1, Max2, Max3, Max1 + Max2 + Max3);
}