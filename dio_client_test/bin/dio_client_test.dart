import 'package:dio/dio.dart';

void getHttp(String port) async {
  try {
    Dio dio = Dio();
    dio.options.headers["Connection"] = "close";
    Response response = await dio.get("http://127.0.0.1:${port}");
    print(response.data);
  } catch (e) {
    print(e);
  }
}

void main(List<String> args) async {
  await getHttp(args[0]);
}
