#! /usr/bin/env python3
#
# Wrapper needed by buidozer who insists on the main module being
# called main.py
#
# by torstein@skybert.net
#
import edward

if __name__ == "__main__":
    edward.main()
