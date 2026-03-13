# RadPageView GotFocus issue

https://chat.openai.com/c/68966e45-a9b8-8323-9592-23fde0922256

## USER
so my GotFocus radpageview isnt firing.    guiPageView_Pending.GotFocus += RadPageGotFocus;

   guiPageView_Processing.GotFocus += RadPageGotFocus;

   guiPageView_InRoute.GotFocus += RadPageGotFocus;

   guiPageView_Complete.GotFocus += RadPageGotFocus;

   guiPageView_Abandoned.GotFocus += RadPageGotFocus;

## ASSISTANT
When the `GotFocus` event handler does not fire on a `RadPageView`, it typically indicates that the control is either not focusable in the way expected or that another component is intercepting focus behavior. The following considerations may help you diagnose and resolve the issue:

### 1. **RadPageView is not inherently focusable**
`RadPageView` (from Telerik WinForms controls) does not natively receive input focus in a way that triggers `GotFocus`—this is by design. Instead, its child pages or controls typically receive focus.

### 2. **Use `SelectedPageChanged` instead**
If your intent is to capture when a different page is selected, use the `SelectedPageChanged` or `SelectedPageChanging` event of the `RadPageView` control:

```csharp
guiPageView_Pending.SelectedPageChanged += RadPageView_SelectedPageChanged;
```

This is more appropriate for monitoring user interaction with different tabs or views.

### 3. **Focus can be consumed by child controls**
If child controls within a `RadPageViewPage` are taking the focus directly, `GotFocus` on the parent page may not fire at all. You might consider subscribing to focus events on specific inner controls instead.

### 4. **Alternative: override `OnEnter` / `OnLeave`**
You may get more consistent behavior using the `Enter` and `Leave` events:

```csharp
guiPageView_Pending.Enter += RadPage_Enter;
```

These are higher-level events that sometimes provide more reliable hooks for user interaction transitions.

### Recommendation
Refactor to use `SelectedPageChanged`, unless you have a specific focus-based need that applies to inner controls. `GotFocus` on the `RadPageView` object is not guaranteed to behave reliably due to focus model constraints in WinForms and Telerik controls.

Let me know if you would like a code sample or help debugging a specific interaction behavior.

## USER
give me the switch method for this guiPageView_Pending.SelectedPageChanged += RadPageView_SelectedPageChanged;


## Thoughts
It seems like the user is asking for a switch statement in the `RadPageView_SelectedPageChanged` event method, to differentiate between selected pages. This can be done using `e.Page.Name` to check the name of the page, like:

```csharp
switch(e.Page.Name) 
{
    case "guiPageView_Pending":
        break;
    case "guiPageView_Processing":
        break;
    // Add more cases as necessary
}
```

Alternatively, you can simplify by using `e.Page.Text` if pages have titles. I'll offer both code examples with clear explanations.
It seems like the user may be trying to handle page changes for multiple `RadPageView` controls (such as `guiPageView_Pending`, `guiPageView_Processing`, etc.), but they're using the same event handler for the `SelectedPageChanged` event. This is a bit odd because usually, you'd use a single `RadPageView` with multiple pages. They want a solution where a single method handles page selection changes for all of these controls.

I'll confirm how to efficiently hook up one event handler for each control and provide the necessary switch case approach.

## ASSISTANT
```csharp
private void RadPageView_SelectedPageChanged(object sender, Telerik.WinControls.UI.PageViewEventArgs e)
{
    // Identify which page has become selected
    var selectedPage = e.Page;

    // Dispatch logic based on the Name (or Text/Tag) of the selected page
    switch (selectedPage.Name)
    {
        case nameof(guiPageView_Pending):
            HandlePendingPage();
            break;

        case nameof(guiPageView_Processing):
            HandleProcessingPage();
            break;

        case nameof(guiPageView_InRoute):
            HandleInRoutePage();
            break;

        case nameof(guiPageView_Complete):
            HandleCompletePage();
            break;

        case nameof(guiPageView_Abandoned):
            HandleAbandonedPage();
            break;

        default:
            // Optional: handle unexpected pages
            HandleUnknownPage(selectedPage);
            break;
    }
}

// Example handler methods
private void HandlePendingPage()
{
    // TODO: insert logic for Pending view
}

private void HandleProcessingPage()
{
    // TODO: insert logic for Processing view
}

private void HandleInRoutePage()
{
    // TODO: insert logic for In-Route view
}

private void HandleCompletePage()
{
    // TODO: insert logic for Complete view
}

private void HandleAbandonedPage()
{
    // TODO: insert logic for Abandoned view
}

private void HandleUnknownPage(RadPageViewPage page)
{
    // TODO: insert fallback or logging
}
```

**Explanation of key points**  
1. **Event signature**: The `SelectedPageChanged` handler receives a `PageViewEventArgs` (`e`) whose `.Page` property is the newly selected `RadPageViewPage`.  
2. **Switch on `.Name`**: By using `selectedPage.Name` (or, if preferred, `.Text` or a custom `.Tag`), branching logic remains clear and maintainable.  
3. **Helper methods**: Extracting each case’s behavior into its own method (e.g. `HandlePendingPage`) improves readability and adheres to single-responsibility principles.  
4. **Default case**: It is prudent to include a `default` branch for logging or error-handling should an unexpected page ever be selected.

## USER
ok we have to query the incoming JobDto to get the subdata. I want the grid to have the Consinee Name, Shipper name and Account Name, Internal Job ID,  pickup date and time, delivery date and time. 
  var jobs = await _jobViewModel.GetIncomingJobs();

  if (jobs.Success)

  {

      guiGRID_Pendiing.DataSource = jobs.Collection;

  }using Logistix.ApplicationLayer.Models.Context.Account; 
using Logistix.ApplicationLayer.Models.Context.Billing;

using Logistix.ApplicationLayer.Models.Context.Dispatch;

using Logistix.ApplicationLayer.Models.Context.Inventory;

using Logistix.ApplicationLayer.Models.Context.Invoice;

using Logistix.ApplicationLayer.Models.Context.RateTable;

using Logistix.ApplicationLayer.Models.Context.Routing;

using Logistix.Infrastructure.Entities.Context.Dispatch;

using Logistix.Infrastructure.Entities.Context.Inventory;

using Logistix.Infrastructure.Entities.Context.Jobs;

using Logistix.Infrastructure.Entities.Context.Routing;

using System;

using System.Collections.Generic;

using System.ComponentModel.DataAnnotations;

using System.Linq;

using System.Text;

using System.Text.Json;

using System.Threading.Tasks;



namespace Logistix.ApplicationLayer.Models.Context.Jobs

{

    public class JobDto : BaseDto

    {

        [Required]

        public string JobInternalID { get; set; } = string.Empty;



        [Required]

        public Guid AccountGUID { get; set; }



        [Required]

        public Guid ShipperGUID { get; set; }



        [Required]

        public Guid ConsigneeGUID { get; set; }



        public byte[]? JobBlobData { get; set; }



        [Required]

        public string DateCreated { get; set; } = DateTime.MinValue.ToString();



        [Required]

        public BillingDto BillingJson { get; set; } = new BillingDto();



        [Required]

        public InvoiceDto InvoiceJson { get; set; } = new InvoiceDto();



        [Required]

        public RoutingDto RoutingJson { get; set; } = new RoutingDto();



        [Required]

        public DispatchDto DispatchJson { get; set; } = new DispatchDto();



        [Required]

        public InventoryDto InventoryJson { get; set; } = new InventoryDto();



        [Required]

        public JobMetaDataDto JobMetaData { get; set; } = new JobMetaDataDto();



        [Required]

        public ClientDto CustomerJsonData { get; set; } = new ClientDto();



        [Required]

        public ShipperDto ShipperJsonData { get; set; } = new ShipperDto();



        [Required]

        public ConsigneeDto ConsigneeJsonData { get; set; } = new ConsigneeDto();



        [Required]

        public JobDetails JobJsonData { get; set; } = new JobDetails();

    }



    public class JobMetaDataDto

    {

        [Required]

        public Guid AccountGUID { get; set; }



        [Required]

        public Guid ShipperGUID { get; set; }



        [Required]

        public Guid ConsigneeGUID { get; set; }



        [Required]

        public double TotalCost { get; set; }



        [Required]

        public int TotalPieces { get; set; }



        [Required]

        public double TotalWeight { get; set; }



        [Required]

        public bool HazmatLoad { get; set; }



        [Required]

        public string DeliveryPriority { get; set; }



        [Required]

        public DateOnly DeliveryDate { get; set; }



        [Required]

        public TimeOnly DeliveryTime { get; set; }



        [Required]

        public DateOnly PickupDate { get; set; }



        [Required]

        public TimeOnly PickupTime { get; set; }



        [Required]

        public string GeoLocation { get; set; }



        [Required]

        public string AccountsPayable { get; set; }

    }



    public class JobDetails

    {

        [Required]

        public string AccountAddress { get; set; }



        [Required]

        public string ShipperAddress { get; set; }



        [Required]

        public string ShipperZipCode { get; set; }



        [Required]

        public string ConsigneeAddress { get; set; }



        [Required]

        public string ConsigneeZipCode { get; set; }



        [Required]

        public bool StoreInInventory { get; set; }



        [Required]

        public List<JobDocuments> JobDocuments { get; set; }



        [Required]

        public List<LoadItem> LoadItems { get; set; } = new List<LoadItem>();



        [Required]

        public DateOnly DeliveryDate { get; set; }



        [Required]

        public DateOnly PickupDate { get; set; }



        [Required]

        public TimeOnly PickupTime { get; set; }



        [Required]

        public TimeOnly DeliveryTime { get; set; }



        public string DeliveryPriority { get; set; }

        public string AccountsPayable { get; set; }

        public string ReferenceNum1 { get; set; }

        public string ReferenceNum2 { get; set; }

        public string QuoteNumber { get; set; }

        public string RateTableOverideReason { get; set; }



        //Job Totals

        public int TotalItemCount { get; set; }



        public decimal TotalDistance { get; set; }

        public decimal TotalCostAccessorials { get; set; }

        public decimal FuelSureCharge { get; set; }

        public decimal TotalWeight { get; set; }



        //Accessorials

        public List<ZoneAccessorialDto> AccessorialList { get; set; }



        //Temp Fields

        public Guid RateTableGuid { get; set; }

        public PricingRuleDto PricingRule { get; set; }

        public string ZoneZipCode { get; set; }

        public string DeliveryType { get; set; }

        public string DriverNotes { get; set; }

        public string JobNotes { get; set; }

        public decimal SubTotal { get; set; }

        public decimal FuleSubCharge { get; set; }

        public decimal TotalCost { get; set; }

    }



    public class JobDocuments

    {

        public string DocName { get; set; }

        public string DocFileName { get; set; }

        public string DocFileSize { get; set; }

    }



    public class LoadItem()

    {

        public int Pieces { get; set; } = 0;

        public int Weight { get; set; } = 0;

        public string LoadType { get; set; }

        public string BlNumber { get; set; }

        public decimal Cost { get; set; }

        public string Description { get; set; }

        public string Note { get; set; }

    }

}

## Thoughts
The user wants to customize a grid to display specific fields from a JobDto list. The list includes fields like Consignee Name, Shipper Name, Account Name, and more. I think using LINQ to project relevant properties into an anonymous type or a view model is the best approach. I'll ensure the properties like ConsigneeDto.Name, ShipperJsonData.Name, and CustomerJsonData are handled correctly. But how to get Account Name? There seems to be a mixup with the Account info in JobDto—I'll need to confirm the right source for that data.

## Thoughts
The developer's message gives some direction, but the search didn’t find the exact file with relevant property names for the grid columns. I'm guessing that the properties like Name for ConsigneeDto, ShipperDto, and AccountName for ClientDto are in specific namespaces. I need to check the definitions for these classes. To move forward, I’ll inspect the code for these models, starting with searching for ConsigneeDto to gather the correct class definitions and their properties.

## ASSISTANT
```csharp
// Define (optionally) a small DTO for clarity
public class JobGridRow
{
    public string ConsigneeName      { get; set; }
    public string ShipperName       { get; set; }
    public string AccountName       { get; set; }
    public string InternalJobId     { get; set; }
    public DateTime PickupDateTime  { get; set; }
    public DateTime DeliveryDateTime{ get; set; }
}

// In your async method:
var jobsResult = await _jobViewModel.GetIncomingJobs();
if (jobsResult.Success)
{
    // Project the JobDto list into only the fields you need
    var gridData = jobsResult.Collection
        .Select(j => new JobGridRow
        {
            ConsigneeName       = j.ConsigneeJsonData.Name,
            ShipperName         = j.ShipperJsonData.Name,
            AccountName         = j.CustomerJsonData.Name,
            InternalJobId       = j.JobInternalID,
            PickupDateTime      = j.JobMetaData.PickupDate
                                        .ToDateTime(j.JobMetaData.PickupTime),
            DeliveryDateTime    = j.JobMetaData.DeliveryDate
                                        .ToDateTime(j.JobMetaData.DeliveryTime)
        })
        .ToList();

    guiGRID_Pendiing.DataSource = gridData;
    guiGRID_Pendiing.AutoGenerateColumns = false;

    // (Re)define your columns so they bind to the properties above:
    guiGRID_Pendiing.Columns.Clear();
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("ConsigneeName")    { HeaderText = "Consignee" });
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("ShipperName")      { HeaderText = "Shipper" });
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("AccountName")      { HeaderText = "Account" });
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("InternalJobId")    { HeaderText = "Job ID" });
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("PickupDateTime")   
    { 
        HeaderText = "Pickup", 
        FormatString = "{0:g}" 
    });
    guiGRID_Pendiing.Columns.Add(new GridViewTextBoxColumn("DeliveryDateTime")
    { 
        HeaderText = "Delivery", 
        FormatString = "{0:g}" 
    });
}
```

**Notes:**  
1. **Projection**: By using `.Select(…)` you extract only the six values the grid needs, avoiding overbinding the entire DTO.  
2. **DateOnly + TimeOnly**: In .NET 6+ you can call `DateOnly.ToDateTime(TimeOnly)` to combine date and time into a `DateTime`.  
3. **Custom DTO vs. Anonymous Type**: Defining `JobGridRow` improves readability and maintainability; you could also project to an anonymous type if you prefer.  
4. **Column Setup**: Turning off auto-generated columns and then manually adding each column lets you control headers and formatting (e.g. general date/time with `{0:g}`).

## USER
how do i set the grid to auto grow or autofill

## ASSISTANT
For a **Telerik RadGridView**, you can make the columns automatically expand to fill the width (or auto-size to content) by setting the `AutoSizeColumnsMode` property.  

If you want **all columns to grow and fill the control**:  
```csharp
guiGRID_Pendiing.AutoSizeColumnsMode = GridViewAutoSizeColumnsMode.Fill;
```

If you want **columns to fit their content**:  
```csharp
guiGRID_Pendiing.AutoSizeColumnsMode = GridViewAutoSizeColumnsMode.AllCells;
```

If you want **just a single column** to fill the remaining space:  
```csharp
guiGRID_Pendiing.Columns["ConsigneeName"].BestFit();
```
or:
```csharp
guiGRID_Pendiing.Columns["ConsigneeName"].Width = guiGRID_Pendiing.Width;
```

**Common fill settings I use in production:**
```csharp
guiGRID_Pendiing.AutoGenerateColumns = false;
guiGRID_Pendiing.AutoSizeColumnsMode = GridViewAutoSizeColumnsMode.Fill;

// Optional: proportionally set FillWeight per column
guiGRID_Pendiing.Columns["ConsigneeName"].Width = 200;
guiGRID_Pendiing.Columns["ShipperName"].Width   = 200;
```

If you want it **to grow with the form size change**, make sure you also set:
```csharp
guiGRID_Pendiing.Dock = DockStyle.Fill;
```
so it resizes with the parent container.  

---

If you tell me whether you want it **fit-to-content** or **fill available space evenly**, I can give you the exact config for your pending jobs grid.

