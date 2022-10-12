use std::ffi::CString;
use std::mem;


#[no_mangle]
pub extern fn lib_test() {
    println!("Hello from the library!");
}

#[no_mangle]
pub extern fn ReturnTheString(name: *const i8) -> *const i8 {
    return name;
}

#[no_mangle]
pub extern fn ReturnHelloWorld() -> *const i8 {
    let s = CString::new("Hello!").unwrap();
    let ptr = s.as_ptr();
    mem::forget(s);
    return ptr;
}

#[no_mangle]
pub extern fn ReturnTheString1(my_name: &[u8; 21]) -> &[u8; 21] {

    return my_name;
}

#[no_mangle]
pub extern fn Return111() -> i32 {
    return 111;
}