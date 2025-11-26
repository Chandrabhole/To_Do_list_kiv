from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty

class ToDoLayout(BoxLayout):
    tasks = ListProperty([])
    task_display = StringProperty("")

    def add_task(self):
        text = self.ids.task_input.text.strip()
        if text:
            self.tasks.append({"task": text, "completed": False})
            self.ids.task_input.text = ""
        self.update_display()

    def mark_completed(self):
        num = self.ids.task_no.text.strip()
        if num.isdigit() and 1 <= int(num) <= len(self.tasks):
            self.tasks[int(num) - 1]["completed"] = True
        self.ids.task_no.text = ""
        self.update_display()

    def delete_task(self):
        num = self.ids.task_no.text.strip()
        if num.isdigit() and 1 <= int(num) <= len(self.tasks):
            self.tasks.pop(int(num) - 1)
        self.ids.task_no.text = ""
        self.update_display()

    def update_display(self):
        self.task_display = "\n".join(
            [f"{i+1}. {'[✔️]' if t['completed'] else '[ ]'} {t['task']}" for i, t in enumerate(self.tasks)]
        )


class ToDoApp(App):
    def build(self):
        return ToDoLayout()

if __name__ == "__main__":
    ToDoApp().run()
