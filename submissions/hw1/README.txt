This sample test script generator can be run in the shell with the command
    python3 generate_tests.py
which will create 16 sets of input/output files
    in1.txt, out1.txt, in2.txt, out2.txt, ...

To test a specific test case, redirect the input into your program and diff
against the expected output. For example, with the first test case, run
    python3 SMTPserver.py < in1.txt > myout1.txt
    diff out1.txt myout1.txt
and the diff command should produce no output if your implementation is correct.

If your implementation is not correct, the diff output will show you where the
two files differ. If you are not familiar with diff's syntax, you might find the
side-by-side option "-y" to be useful. For example,
    diff -y out1.txt myout1.txt

To (automatically) run all 16 commands in sequence in bash, you can execute
    for i in {1..16}; do
        python3 SMTPserver.py < "in$i.txt" > "myout$i.txt"
    done
rather than running each command one at a time.

The test script generator produces two additional files, "<smithfd@cs.unc.edu>"
and "<firstname_lastname@gmail.com>". These contain the expected contents of
forward/<smithfd@cs.unc.edu> and forward/<firstname_lastname@gmail.com> after
all tests are run in sequence (and the forward/... files were initially empty), so
    diff "<firstname_lastname@gmail.com>" "forward/<firstname_lastname@gmail.com>"
    diff "<smithfd@cs.unc.edu>" "forward/<smithfd@cs.unc.edu>"
should both produce no output.

