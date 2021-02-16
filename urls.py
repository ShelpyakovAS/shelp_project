import views


urls_routes = {
    '/': views.Index(),
    '/about/': views.About(),
    '/other/': views.Other(),
    '/control-panel/': views.ControlPanel(),
    '/create-category/': views.CreateCategory(),
    '/create-curse/': views.CreateCurse(),
    '/curses/': views.Curses()
}