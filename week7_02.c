#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <time.h>

void f () {
    pid_t pid = fork();
    double child = 0, parent = 0;
    switch (pid)
    {
        case 0:
            int neg = 0;
            for (double i=31.0; i<60.0; i+=2) {
                child += (1/i) * pow(-1, ++neg);
            }
            int ret = child * -10000.0;
            _exit(ret);
            break;
        
        default:
            neg = 0;
            for (double i=1.0; i<30.0; i+=2) {
                parent += ((1/i) * pow(-1, neg++));
            }
            printf("%lf\n", parent);
            int status;
            wait(&status);
            int exitCode = WEXITSTATUS(status);
            printf("%d\n", exitCode);
            double child = exitCode / -10000.0;
            printf("%lf\n", child);
            double pi = (parent + child) * 4;
            printf("%lf\n", pi);
    }
}

int main () {
    struct timespec st = {0, 0};
    struct timespec et = {0, 0};
    clock_gettime(CLOCK_REALTIME, &st);

    f();
    
    clock_gettime(CLOCK_REALTIME, &et);
    printf("%ld ns\n",(et.tv_nsec-st.tv_nsec));

    /* ----------------------------------------- */

    st.tv_sec = 0; st.tv_nsec = 0;
    et.tv_sec = 0; et.tv_nsec = 0; 
    clock_gettime(CLOCK_REALTIME, &st);

    double tmp = 0;
    int neg = 0;
    for (double i=1; i<60; i+=2) {
        tmp += ((1/i) * pow(-1, neg++));
    }
    printf("%lf\n", tmp*4.0);
    clock_gettime(CLOCK_REALTIME, &et);
    printf("%ld ns\n",(et.tv_nsec-st.tv_nsec));
    return 0;
}