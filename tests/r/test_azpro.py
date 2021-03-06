from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.azpro import azpro


def test_azpro():
  """Test module azpro.py by downloading
   azpro.csv and testing shape of
   extracted data has 3589 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = azpro(test_path)
  try:
    assert x_train.shape == (3589, 6)
  except:
    shutil.rmtree(test_path)
    raise()
