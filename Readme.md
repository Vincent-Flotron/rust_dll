# Building a rust dynamic library and using it from Python script




## Importants steps



### From Rust side

In the file "Cargo.toml", add the lines

```c++
[lib]
crate-type = ["cdylib"]
```




Then compile it using the terminal:

```bash
cargo build --lib
```



It will generate the dynamic library here:
```
.\target\debug\rust_dll.dll
```





### From the Python side

Run the Python script "main.py"





## Importants links

[Creating a Rust dll](https://gist.github.com/CoolOppo/67b452c125bb0db3212a9fbc44c84245)
[Calling a Rust dll from Python script](https://stackoverflow.com/questions/30510764/returning-a-string-from-rust-function-to-python)
