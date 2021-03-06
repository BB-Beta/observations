from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sleepstudy import sleepstudy


def test_sleepstudy():
  """Test module sleepstudy.py by downloading
   sleepstudy.csv and testing shape of
   extracted data has 180 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sleepstudy(test_path)
  try:
    assert x_train.shape == (180, 3)
  except:
    shutil.rmtree(test_path)
    raise()
