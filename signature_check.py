import cv2

def orb_sim(path1, path2):
  img1 = cv2.imread(path1)
  img2 = cv2.imread(path2)

  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  img1 = cv2.resize(img1, (300, 300))
  img2 = cv2.resize(img2, (300, 300))
  
  orb = cv2.ORB_create()

  kp_a, desc_a = orb.detectAndCompute(img1, None)
  kp_b, desc_b = orb.detectAndCompute(img2, None)

  bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
  matches = bf.match(desc_a, desc_b)

  similar_regions = [i for i in matches if i.distance < 50]  
  if len(matches) == 0:
    return 0
  return len(similar_regions) / len(matches)
