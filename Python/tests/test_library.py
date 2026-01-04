import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

pytest.skip("Tests moved to `library/tests`, keep this file for compatibility.", allow_module_level=True)
