#define CATCH_CONFIG_MAIN  
#include "../3party/Catch2/include/catch.hpp"

int reverse(int x) 
{
    const int MY_MAX = 2147483647;
    const int MY_MIN = -2147483648;
    int sign = +1 | (x >> (sizeof(int)*8 - 1));

    if (x == MY_MIN || x == MY_MAX) return 0;
    int num = x * sign;

    if (num >= 0 and num <= 9) return num * sign;

    int i = 1;
    int total = 0;
    while (i < 11 and num != 0)
    {
        int r = num % 10;
        num = num / 10;
        int temp = (MY_MAX - r) / 10;
        if ( temp < total) return 0;
        total = total * 10 + r; 
        i++;
    }

    if (i == 11 && num != 0) return 0;
    return total * sign;
};

TEST_CASE( "Reverse number", "[reverse]" ) 
{
    REQUIRE( reverse(123) == 321 );
    REQUIRE( reverse(-123) == -321 );
    REQUIRE( reverse(0) == 0 );
    REQUIRE( reverse(120) == 21 );
    REQUIRE( reverse(1234567899) == 0 );
    REQUIRE( reverse(1234567891) == 1987654321 );
    REQUIRE( reverse(-2147483648) == 0 );
    REQUIRE( reverse(2147483647) == 0 );
}

