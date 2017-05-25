rule exe
{
    strings:
        $pdf  = "MZ"
    condition:
        any of them
}