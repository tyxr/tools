from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, fbeta_score

y_true = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 27, 28, 29, 29, 29, 30, 30, 30, 31, 31, 32, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 70, 70, 70, 71, 71, 71, 72, 72, 72, 73, 73, 73, 74, 74, 74, 75, 75, 76, 76, 76, 76, 77, 77, 77, 78, 78, 78, 78, 79, 79, 79, 80, 80, 81, 81, 82, 82, 82, 83, 83, 84, 84, 84, 85, 85, 85, 86, 86, 87, 87, 87, 88, 88, 88, 89, 89, 89, 90, 90, 90, 91, 91, 91, 92, 92, 92, 93, 93, 93, 93, 94, 94, 94, 94, 95, 95, 95, 95, 95, 96, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100, 100, 101, 101, 101, 102, 102, 102, 102, 103, 103, 103, 104, 104, 104, 105, 105, 106, 106, 107, 107, 108, 108, 108, 109, 109, 109, 110, 110, 111, 111, 112, 112, 113, 113, 114, 114, 115, 115, 115, 116, 116, 116, 117, 117, 118, 118, 119, 119, 119, 120, 120, 121, 121, 122, 122, 123, 123, 123, 124, 124, 124, 125, 125, 125, 126, 126, 126, 127, 127, 127, 128, 128, 129, 129, 130, 130, 131, 131, 131, 131, 132, 132, 132, 133, 133, 134, 134, 135, 135, 135, 136, 136, 136, 137, 137, 138, 138, 138, 139, 139, 139, 140, 140, 141, 141, 141, 141, 142, 142, 142, 143, 143, 143, 144, 144, 144, 145, 145, 145, 146, 146, 146, 147, 147, 148, 148, 148, 149, 149, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 228, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 258, 258, 259, 259, 259, 260, 261, 262, 263, 264, 264, 265, 265, 266, 267, 268, 269, 270, 271, 271, 271, 272, 273, 273, 274, 275, 275, 276, 276, 277, 277, 278, 278, 279, 280, 280, 281, 281, 281, 282, 282, 283, 284, 285, 286, 287, 288, 289, 290, 290, 291, 292, 293, 294, 294, 295, 295, 295, 296, 296, 296, 296, 297, 297, 297, 298, 299, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 308, 308, 309, 309, 309, 310, 310, 310, 311, 311, 312, 313, 314, 315, 316, 316, 316, 317, 318, 318, 319, 320, 321, 321, 322, 323, 324, 324, 325, 326, 327, 328, 328, 328, 329, 330, 331, 332, 333, 334, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 345, 345, 346, 346, 346, 347, 347, 347, 348, 348, 349, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386]
y_pred = [0, 20, 20, 46, 3, 52, 5, 6, 384, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 86, 21, 24, 25, 26, 27, 27, 28, 29, 29, 29, 30, 30, 30, 31, 31, 32, 32, 34, 34, 34, 60, 37, 38, 39, 39, 41, 42, 43, 44, 45, 46, 47, 47, 54, 1, 50, 354, 52, 53, 75, 10, 56, 348, 58, 284, 60, 61, 62, 63, 64, 152, 64, 64, 65, 65, 65, 66, 66, 66, 66, 67, 67, 68, 67, 68, 67, 67, 377, 380, 67, 70, 70, 70, 71, 71, 71, 72, 72, 72, 87, 73, 73, 74, 74, 13, 74, 74, 76, 76, 76, 76, 77, 77, 77, 78, 378, 378, 378, 79, 78, 79, 80, 80, 81, 84, 82, 82, 82, 96, 83, 84, 84, 84, 85, 85, 85, 86, 86, 87, 87, 87, 88, 88, 88, 89, 89, 89, 90, 128, 128, 380, 380, 380, 92, 380, 74, 93, 93, 93, 93, 94, 94, 94, 94, 380, 380, 380, 86, 380, 94, 94, 115, 97, 97, 98, 98, 99, 99, 100, 101, 100, 101, 103, 380, 102, 79, 79, 102, 103, 102, 102, 104, 104, 104, 113, 113, 106, 115, 107, 107, 108, 108, 68, 109, 109, 63, 110, 110, 111, 111, 112, 112, 113, 113, 114, 114, 115, 106, 380, 56, 116, 116, 117, 117, 118, 118, 119, 119, 119, 120, 120, 121, 121, 122, 122, 123, 83, 123, 124, 124, 124, 378, 83, 125, 126, 126, 126, 56, 127, 148, 128, 128, 121, 195, 121, 121, 131, 131, 131, 17, 132, 132, 132, 133, 133, 133, 133, 135, 135, 79, 136, 136, 136, 137, 137, 138, 136, 138, 139, 139, 139, 140, 140, 141, 141, 142, 141, 8, 63, 142, 143, 63, 143, 8, 223, 63, 146, 145, 145, 380, 146, 146, 147, 147, 148, 128, 148, 149, 149, 149, 150, 151, 152, 153, 154, 155, 156, 157, 159, 158, 160, 161, 162, 163, 164, 165, 166, 167, 300, 169, 170, 171, 172, 170, 174, 175, 176, 248, 178, 179, 249, 181, 251, 246, 184, 186, 186, 187, 347, 245, 190, 191, 192, 125, 194, 195, 195, 199, 198, 199, 193, 201, 202, 203, 204, 205, 206, 207, 264, 168, 210, 211, 157, 213, 373, 216, 193, 373, 218, 219, 151, 221, 222, 223, 223, 225, 226, 227, 160, 160, 160, 229, 153, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 355, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 258, 258, 259, 259, 259, 260, 261, 264, 263, 264, 264, 265, 265, 266, 267, 268, 269, 327, 271, 176, 380, 272, 345, 276, 267, 313, 313, 345, 345, 277, 280, 282, 278, 279, 280, 279, 281, 281, 281, 282, 292, 283, 284, 285, 286, 287, 288, 282, 290, 290, 291, 210, 293, 349, 294, 295, 295, 295, 296, 296, 296, 296, 297, 297, 297, 298, 299, 299, 300, 264, 302, 303, 304, 305, 306, 307, 314, 176, 308, 309, 309, 309, 310, 310, 310, 311, 311, 312, 373, 314, 315, 316, 316, 316, 317, 318, 318, 319, 320, 321, 321, 322, 323, 324, 324, 325, 326, 329, 328, 328, 328, 329, 328, 331, 332, 333, 331, 331, 335, 336, 337, 338, 339, 340, 369, 342, 343, 344, 345, 345, 345, 346, 346, 346, 347, 347, 347, 348, 348, 349, 294, 350, 351, 352, 353, 354, 355, 84, 357, 358, 359, 360, 361, 362, 282, 363, 365, 366, 367, 368, 370, 370, 33, 372, 373, 374, 375, 376, 377, 378, 380, 380, 381, 382, 383, 384, 385, 386]

print("accuracy_score:",accuracy_score(y_true, y_pred)) # Return the number of correctly classified samples
print("accuracy_score normalize=False:",accuracy_score(y_true, y_pred, normalize=False)) # Return the fraction of correctly classified samples


# Calculate precision score
print("precision_score('macro')",precision_score(y_true, y_pred, average='macro'))
print("precision_score('micro')",precision_score(y_true, y_pred, average='micro'))
#print(precision_score(y_true, y_pred, average=None))


# Calculate recall score
print("recall_score('macro')",recall_score(y_true, y_pred, average='macro'))
print("recall_score('micro')",recall_score(y_true, y_pred, average='micro'))
#print(recall_score(y_true, y_pred, average=None))

# Calculate f1 score
print("f1_score('macro')",f1_score(y_true, y_pred, average='macro'))
print("f1_score('micro')",f1_score(y_true, y_pred, average='micro'))
#print(f1_score(y_true, y_pred, average=None))

# Calculate f beta score
print("fbeta_score('macro', beta=0.5)",fbeta_score(y_true, y_pred, average='macro', beta=0.5))
print("fbeta_score('micro', beta=0.5)",fbeta_score(y_true, y_pred, average='micro', beta=0.5))
#print(fbeta_score(y_true, y_pred, average=None, beta=0.5))
