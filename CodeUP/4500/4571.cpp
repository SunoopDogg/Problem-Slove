#include <iostream> 
#include <cmath> 
using namespace std ; 
int main( void ) 
{ 
   int iN = 0, iM = 0 ; 
   int iStartM = 0 ; 
   int iEndN = 0 ; 
   int iSum = 0 ; 
   int iMinimum = 0 ; 
   cin >> iM  >> iN ; 
   double dRootValue = 0.0f ; 
   if( sqrt( ( double )iM ) > ( int )( sqrt( ( double )iM ) ) ) 
   { 
      iStartM = ( int )( sqrt( ( double )iM ) ) + 1 ; 
   } 
   else 
   { 
      iStartM = ( int )( sqrt( ( double )iM ) ) ; 
   } 
   iEndN = ( int )( sqrt( ( double )iN ) ) ; 
   if( iStartM > iEndN ) 
   { 
      cout << -1 << endl ; 
   } 
   else 
   { 
      iMinimum = iStartM * iStartM ; 
      for( int i = iStartM ; i <= iEndN ; ++i ) 
      { 
         iSum += i * i ; 
      } 
      cout << iSum << endl ; 
      cout << iMinimum << endl ; 
   } 
   return 0 ; 
} 