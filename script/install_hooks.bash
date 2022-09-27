#!/bin/sh
cd .. && cd .git/hooks && ln -s ../../test/run_test_from_hook.bash post-commit && chmod a+x post-commit
