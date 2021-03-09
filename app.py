# 이미지 처리

import streamlit as st

from PIL import Image, ImageFilter, ImageEnhance

from datetime import datetime

# def main()  : 

#     img = Image.open('data/birds.jpg')  # 이미지 가져오기 
#     st.image(img)  

#     option_list =  [ 'Show Image', 'Rotate Image', 'Creat Thumbnail',
#                      'Crop Image', 'Merge Images', 'Flip Image', 'Black & White',
#                       'Filters - Sharpen', 'Filters - Edge Enhance',
#                       'Contrast Image'  ]
#                      # 이러한 기능을 하도록 만든다

#     option =  st.selectbox('옵션을 선택하세요', option_list)

#     if option == 'Show Image' :
#         st.image(img)

#     elif option == 'Rotate Image' :
#         rotated_img = img.rotate(90) # 90 도 회전
#         img.save('data/rotate.png')
#         st.image(rotated_img)                        
    
#     elif option == 'Create Thumbnail' :
#          = (300,300)
#         img.thumbnail( size )
#         img.save('data/thumb.png') 
#         st.image(img)                # 원본 사이즈 바꾸고 data에 thumb.png 로 저장했다   (다른것도 가능 )

#     elif option == 'Crop Image' :      # 이미지 자를 때
#         # 왼쪽 윗부분 부터, 오른쪽 아래 부분 까지 잘라라
#         # 왼쪽 윗부분 좌표 ( 50,100 )
#         # 오른쪽 아래부분 좌표 ( 200,200 )
#         box = ( 50,100,200,200 )
#         cropped_img = img.crop(box)
#         img.save('data/crop.png')
#         st.image(cropped_img)


#     elif option == 'Merge Image' :  # 두개합치는 것
#         pass

#     elif option == 'Flip Image' :   #  이미지 뒤집기 
#         flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT )  
#         st.image(flipped_img)

#     elif option == 'Black & White' :  # 이미지 색상 바꾸기
#         bw = img.convert('1')  # "L" 로쓰면 그레이스케일됨
#         st.image( bw )

#     elif option == 'Filters - Sharpen' :   # 이미지 선명하게
#         sharp_img = img.filter(ImageFilter.SHARPEN)
#         st.image( sharp_img )

#     elif  option == 'Filters - Edge Enhance'  :  # 윤곽선이 진해진다 
#         edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
#         st.image(edge_img)

#     elif option == 'Contrast Image' :        # 대비가 세진다 
#         contrast_img = ImageEnhance.Contrast(img).enhance( 2 )
#         st.image(contrast_img)    

#     










#if __name__ == '__main__' :
#    main()
# import os
# # 디렉토리와 파일을 주면, 해당 디렉토리에 이 파일을 저장하는 함수

# def save_uploaded_file(directory, file) :
#     # 1 . 디렉토리가 있는지 확인하여 , 없으면 만든다.
#     if not os.path.exists(directory) :      
#         os.makedirs(directory)
#     # 2 . 이제는 디렉토리가 있으니까 , 파일을 저장 
#     with open(os.path.join(directory, file.name),  'wb') as f : 
#         f.write(file.getbuffer())
#     return st.success('Saved file : {} in {}'.format(file.name, directory)) 
import os

from datetime import datetime

def load_image(image_file) :
    img = Image.open(image_file)
    return img
                     # 이미지 파일 만들어내는 함수


# 디렉토리와 이미지를 주면, 해당 디렉토리에 이 이미지를 저장하는 함수

def save_uploaded_file(directory, img) :  
    # 1 . 디렉토리가 있는지 확인하여 , 없으면 만든다.
    if not os.path.exists(directory) :      
        os.makedirs(directory)
    # 2 . 이제는 디렉토리가 있으니까 , 파일을 저장 
    filename =  datetime.now().isoformat().replace(':', '-').replace('.', '-')   # 마이크로 세컨드(초) 시간 까지 나와야 한개 한개 다 구분가능 
    img.save( directory + '/' + filename + '.jpg' )                            # 다 하이픈으로 바꿔주니 저장했음
    # 원본이미지를 저장하는것이 아니라 효과를 준 이미지를 저장하므로 img.save( )다
    return st.success('Saved file : {} in {}'.format(filename +'.jpg', directory))

    # 파일명을 a.jpg 로만 하게 되면 아무리 이미지를 받아도 한개의 이미지만 저장된다 
    # 그러니 구분이 가능한건 시간이 제일 좋다 datetime 
                                                     


def main()  : 
         # 2021-03-09 16:23:56.329416
    #print(datetime.now().isoformat())    # 이건 시간을 가져오는지 확인하기 위해 메인에 실행시켜본것
                        # 2021-03-09T16:24:35.372407 
    #1. 파일 업로드 하기
    image_file_list = st.file_uploader('Upload Image', type = ['png', 'jpg', 'jpeg'],
     accept_multiple_files = True) 

    print(image_file_list)  # image_file_list는 리스트다  [첫번째파일, 두번째 파일] 이런형태

    if image_file_list is not None :  # 유저가 입력한 파일이 있으면

        # 2. 각 파일을 이미지로 바꿔줘야 한다  
        # # img 라고하면 1개의 이미지만 받는거고 img_list 이렇게 바꿔야 여러개를 받을수 있다 
           # img_list 형태가 [첫번째 이미지, 두번째 이미지] 이다
        image_list = []   
        
        # 2-1 . 모든 파일이 , image_list 에 이미지로 저장됨 
        for image_file in image_file_list :  # [첫번째 파일, 두번째 파일~~] 이걸 한개씩 꺼내서 이미지로 변환해라 
            img = load_image(image_file)  
            image_list.append(img)   # 이제 [첫번째이미지, 두번째 이미지 ] 이 형태로 나왔음 
        
        # # 3. 이미지를 화면에 확인해 본다
        # for img in image_list :
        #     st.image(img) 

        option_list =  [ 'Show Image', 'Rotate Image', 'Create Thumbnail',
                     'Crop Image', 'Merge Images', 'Flip Image', 'Change color',
                      'Filters - Sharpen', 'Filters - Edge Enhance',
                      'Contrast Image'  ]
                     # 이러한 기능을 하도록 만든다

        option =  st.selectbox('옵션을 선택하세요', option_list)
          
       
        if option == 'Show Image' :
            transformed_img_list = []
            for img in image_list :
                st.image(img)     # 이미지 가져와서 하나씩 찍어보는것
                transformed_img_list.append(img)
            # 화면에 원본이미지를 하나씩 찍어서 다표시된 후에 경로를 지정한다 
            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :   
                # 3. 파일 저장
                for img in transformed_img_list :       
                    save_uploaded_file(directory, img)    
                 
        elif option == 'Rotate Image' :
            #1. 유저가 입력
            degree =  st.number_input('각도입력', 0,360 )   # 0부터 360까지 정수로 입력받을수 있디
            # 2. 모든 이미지를 돌린다
            transformed_img_list = []
            for img in image_list :  # 지금 save 써서 저장했던부분을 반복문 돌리는것
                rotated_img =  img.rotate(degree)
                st.image(rotated_img)   # rotated_img = 이미지 두개를 돌렸는데 마지막 이미지가 회전된것이다
                                        # 이건 리스트형태가 아니었는데 위에서 transformed_img_list = [] 이렇게 빈 리스트를
                                        # 만들어 append 하여 로테이트로 변형된 이미지를 저장한다 
                transformed_img_list.append(rotated_img)                        
            
            # 화면에 이미지를 돌린것이 다표시된 후에 경로를 지정한다 
            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장
                for img in transformed_img_list :       
                    save_uploaded_file(directory, img)    
                    # 입력페이지에 파일경로 입력을 rotation 으로 하면 저장 되었다고 뜬다 

            


            # 
                                    
    
        elif option == 'Create Thumbnail' :   
            # 이미지의 사이즈를 알아야겠다.
            # print(img.size)  
            #st.write(img.size) # 둘다 똑같음
            # 가장 작은 이미지를 사이즈를 찾아 그것을 기준으로 하는것이 좋을 듯 하다
            
            # 썸네일 크기를 정함 
            width = st.number_input('width 입력', 1, 100 )   # 이미지 여러개를 다 줄이려 하니 사이즈를 일부러 맞췄다
            height =  st.number_input( 'height 입력', 1, 100 )
            size = ( width, height )

            # 이미지가 한개가 아니니 원본이미지 리스트에 들어있는 이미지를 가져와서 썸네일 하라 size 로 
            # 빈 리스트를 만들어 반복문을 돌린것을 저장시켜라 
            transformed_img_list = []
            for img in image_list :
                             # 이미지 썸네일하면 이미지 자체를 바꿔버리는 것이라 변수에 저장하면 안된다 
                img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)
            
            # 저장은 여기서 

            # 화면에 이미지를 돌린것이 다표시된 후에 경로를 지정한다 
            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장
                for img in transformed_img_list :       
                    save_uploaded_file(directory, img)    

    
#             

#         elif option == 'Crop Image' :      # 이미지 자를 때
#         # 왼쪽 윗부분 부터, 오른쪽 아래 부분 까지 잘라라
#         # 왼쪽 윗부분 좌표 ( 50,10 )
#         # 너비 x축으로, 깊이 y축으로 계산한 종료좌표(200,200)
#         # 시작 좌표 + ( 너비 , 높이 ) =>  크랍 종료 좌표
#             start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1 )  # 가로 세로 사이즈가 다르니 이렇게 해야함 
#             start_y =  st.number_input( '시작 y 좌표', 0, img.size[1]-1 ) 
#             # start_x가 0~0까지 이고 start_y가 0~1 까지 면 이미지를 자를 때 전체다 자를 수도 있으니 예외처리를 한것
#             max_width = img.size[0] - start_x
#             max_height = img.size[0] - start_y   # 예외처리 한것 
            
#             width = st.number_input('width 입력', 1, max_width ) # 너비가 0부터 시작일수는 없으니 1 임
#             height =  st.number_input( 'height 입력', 1, max_height )    



#             box = ( start_x, start_y, start_x + width, start_y + height )
#             st.write(box)  # crop 이미지가 왜 안보여지는 지 확인한다
#             cropped_img = img.crop(box)
#             # img.save('data/crop.png')
#             st.image(cropped_img)


#         elif option == 'Merge Image' :  # 두개합치는 것    # 오류 

#             merge_file = st.file_uploader('Upload Image', type = ['png', 'jpg', 'jpeg'], key='merge')    
#                                                                                  # 위에 업로더 쓴것과 충돌이 일어나지 않게 키를 머지로 한것
           

#             if merge_img is not None :
#                   # 유저가 입력한 머지 이미지가 있으면      # 오류

#                 merge_img =  Image.open(merge_file)  # 이미지로 바꿔라 

#                 start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1 )  # 가로 세로 사이즈가 다르니 이렇게 해야함 
#                 start_y =  st.number_input( '시작 y 좌표', 0, img.size[1]-1 )

#                 position =  (start_x, start_y)  # 원래 이미지 안쪽에 추가되는게 들어가게 y축 이 원본이미지 y축보다 작아야함 
#                 img.paste(merge_img, position)
#                 st.image(img)

        elif option == 'Flip Image' :   #  이미지 뒤집기    

            status = st.radio('플립 선택', ['FLIP_TOP_BOTTOM', 'FLIP_LEFT_RIGHT'])
            
            if status == 'FLIP_TOP_BOTTOM' :
                transformed_img_list = []
                for img in image_list :

                    flipped_img = img.transpose( Image.FLIP_TOP_BOTTOM )  
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
            
            elif status == 'FLIP_LEFT_RIGHT' :
                transformed_img_list = []
                for img in image_list :

                    flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT )  
            
                    st.image(flipped_img)  # 탑 바텀 이나 왼쪽오른쪽 나오게   # 셀렉트박스 써도됨
                    transformed_img_list.append(flipped_img)
                    # 이러면 화면에만 표시되는것 

            # 저장은 여기서 

            # 화면에 이미지를 돌린것이 다표시된 후에 경로를 지정한다 
            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장
                for img in transformed_img_list :       
                    save_uploaded_file(directory, img)


#         elif option == 'Change Color' :  # 이미지 색상 바꾸기  # 오류

#             status = st.radio('색 변경',
#             ['Color', 'Gray Scale', 'Black & White'] )
            
#             if status == 'Color' :
#                 color = 'RGB'
#             elif status == 'Gray Scale' :
#                 color = 'L'
#             elif status == 'Black & White' :
#                 color = '1'
            
#             bw = img.convert('1')  # "L" 로쓰면 그레이스케일됨
#             st.image( bw )

#         elif option == 'Filters - Sharpen' :   # 이미지 선명하게
#             sharp_img = img.filter(ImageFilter.SHARPEN)
#             st.image( sharp_img )

#         elif  option == 'Filters - Edge Enhance'  :  # 윤곽선이 진해진다 
#             edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
#             st.image(edge_img)

#         elif option == 'Contrast Image' :        # 대비가 세진다 
#             contrast_img = ImageEnhance.Contrast(img).enhance( 2 )
#             st.image(contrast_img)    

# #3. 여러파일을 변환 할 수 있도록 수정
# #    각 옵션마다 저장하기 버튼이 잇어서 ,
# #    버튼 누르면 저장되도록
# #    저장시에는, 디렉토리 이름을 유저가 직접 입력하여 저장
   
   
#     import os
# # 디렉토리와 파일을 주면, 해당 디렉토리에 이 파일을 저장하는 함수

# def save_uploaded_file(directory, file) :
#     # 1 . 디렉토리가 있는지 확인하여 , 없으면 만든다.
#     if not os.path.exists(directory) :      
#         os.makedirs(directory)
#     # 2 . 이제는 디렉토리가 있으니까 , 파일을 저장 
#     with open(os.path.join(directory, file.name),  'wb') as f : 
#         f.write(file.getbuffer())
#     return st.success('Saved file : {} in {}'.format(file.name, directory)) 



if __name__ == '__main__' :
    main()
