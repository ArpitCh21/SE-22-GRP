#!/bin/bash
cd .. && cd .. && cd .git/hooks && ln -s ../../test/run_test_from_hook.bash post-commit && chmod 755 post-commit
