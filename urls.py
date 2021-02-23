import views


urls_routes = {
    '/': views.Index(),
    '/about/': views.About(),
    '/other/': views.Other(),
    '/control-panel/': views.ControlPanel(),
    '/create-category/': views.CreateCategory(),
    '/create-curse/': views.CreateCurse(),
    '/curses/': views.Courses(),
    '/create-user/': views.CreateUser(),
    '/change-course/': views.ChangeCourse(),
    '/enroll-course/': views.EnrollCourse()
}
