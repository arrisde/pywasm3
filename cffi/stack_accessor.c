#include "m3_core.h"
#include "m3_env.h"
#include "wasm3.h"
#include "stack_accessor.h"


i32 m3_GetResultI32 (IM3Runtime i_runtime)
{
    return *(i32*)(i_runtime->stack);
}

i64 m3_GetResultI64 (IM3Runtime i_runtime)
{
    return *(i64*)(i_runtime->stack);
}

f32 m3_GetResultF32 (IM3Runtime i_runtime)
{
    return *(f32*)(i_runtime->stack);
}

f64 m3_GetResultF64 (IM3Runtime i_runtime)
{
    return *(f64*)(i_runtime->stack);
}