#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
  double y, t;
  double arr[1005];
  double yarr[1005];
  double r[30] = {0};
  for (int i = 0; i < 500; i++)
  {
    y = rand() / (double)RAND_MAX;
    yarr[i] = y;
    if (y > 0 && y < (1 / 2))
    {
      arr[i] = 1;
    }
    else
    {
      if (y > 1 / 2)
        arr[i] = 2;
    }
  }
  for (int j = 0; j < 500; j++)
  {
    for (int i = 0; i < 20; i++)
    {
      if (arr[j] > i * 0.1 && arr[j] < (i * 0.1) + 0.1)
      {
        r[i] += 1;
      }
    }
  }
  for (int i = 0; i < 20; i++)
  {
    std::cout << r[i] << endl;
  }
  system("pause");
  return 0;
}
