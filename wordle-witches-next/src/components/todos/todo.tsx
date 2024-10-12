import TodoData from "./todo-data";
import TodoCheckBox from "./todo-checkbox";
import DeleteTodo from "./delete-todo";

import { editTodo } from "@/actions/todos/actions";
import type { Todo } from "@/lib/interface";

export default async function Todo({ todo }: { todo: Todo }) {
  return (
    <div className="flex gap-2 items-center">
      <form
        className="flex flex-1 gap-2 items-center"
        action={async () => {
          "use server";
          await editTodo(todo);
        }}
      >
        <TodoCheckBox todo={todo} />
        <TodoData todo={todo} />
      </form>
      <DeleteTodo id={todo.id} />
    </div>
  );
}
