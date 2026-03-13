# RadioButton Grouping Explained

https://chat.openai.com/c/67f41a9c-4824-8011-b27a-9a6832797ba7

## USER
so how are radiobuttons grouped?

## ASSISTANT
RadioButtons are grouped based on **their container**. Here's how it works depending on the platform:

---

### **Windows Forms (WinForms)**

In WinForms:
- **RadioButtons in the same container (e.g., a `Panel`, `GroupBox`, or `Form`) are automatically grouped.**
- Selecting one `RadioButton` will unselect others within the same container.
- To create independent groups of `RadioButtons`, place them in separate containers (like different `GroupBox`es or `Panel`s).

**Example:**

```csharp
GroupBox group1 = new GroupBox();
RadioButton rb1 = new RadioButton();
RadioButton rb2 = new RadioButton();

GroupBox group2 = new GroupBox();
RadioButton rb3 = new RadioButton();
RadioButton rb4 = new RadioButton();

// rb1 and rb2 belong to group1
group1.Controls.Add(rb1);
group1.Controls.Add(rb2);

// rb3 and rb4 belong to group2
group2.Controls.Add(rb3);
group2.Controls.Add(rb4);
```

Now `rb1` and `rb2` are grouped together, and `rb3` and `rb4` are grouped together independently.

---

### **Web (HTML)**

In HTML:
- Grouping is done using the **`name` attribute**.
- Radio buttons that share the same `name` are grouped together.

**Example:**

```html
<input type="radio" name="group1" value="A"> A
<input type="radio" name="group1" value="B"> B

<input type="radio" name="group2" value="X"> X
<input type="radio" name="group2" value="Y"> Y
```

Here, selecting an option from `group1` doesn’t affect `group2`.

---

If you’re asking in the context of Telerik or a specific UI framework, let me know—I'll tailor it.

