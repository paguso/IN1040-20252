#include <cstddef>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <ctime>
#include <iostream>
#include <random>
#include <chrono>

using namespace std;
using u32    = uint_least32_t; 
using engine = std::mt19937;
using unifdist26 = std::uniform_int_distribution< u32 >;

#define RANDOM_CHAR ('a' +  distribute(rng))

u32 single_run(engine &rng, u32 typed_chars = 100000000) {
    unifdist26 distribute( 0, 26 );
    assert( 5 <= typed_chars);
    const char *breno = "breno";
    char window[6] = {'\0', '\0', '\0', '\0', '\0', '\0'};
    u32 i = 0;
    for (i = 0; i < 4; window[i++] = RANDOM_CHAR);
    u32 start = 0;
    u32 success = 0;
    while (i < typed_chars) {
        window[i % 5] = RANDOM_CHAR;
        u32 j = 0;
        while (j < 5) {
            if (window[(start + j) % 5] != breno[j] ) 
            break;
            j++;
        }
        if (j == 5) {
            printf("i=%u st=%d %s\n", i, start, (char*)window);
            success++;
        }
        start = (start + 1) % 5;
        i++;
    }
    return success;
}




int main( int argc, char **argv )
{
    std::random_device os_seed;
    const u32 seed = os_seed();
    engine rng( seed );

    u32 reps = 10;
    if (argc > 1) {
        reps = std::stoi(argv[1]);
    }
    srand(time(0));
    u32 nsucc = 0;
    for (u32 i = 0; i < reps; i++) {
        u32 s = single_run(rng);
        printf("Run #%u count=%u\n", i, s);
        nsucc += s;
    }
    printf("total success = %u\n", nsucc);
    printf("exp success = %f\n", (double)nsucc/(double)reps);
    
}